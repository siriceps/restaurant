from rest_framework import mixins, viewsets
from rest_framework.response import Response

from mycart.models import MyCart
from mycart.serializer import MyCartSerializer, MyCartListSerializer


class ViewToTal(viewsets.ModelViewSet):
    queryset = MyCart.objects.all()
    serializer_class = MyCartSerializer

    action_serializers = {
        'create': MyCartSerializer,
        'list': MyCartListSerializer,
        'retrieve': MyCartSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

    def partial_update(self, request, *args, **kwargs):
        total = self.get_object()
        old_data = MyCart.get_food_menu(total)
        serializer = self.get_serializer(total, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        category = serializer.save()

        if 'sort' in data:
            Category.check_sort(category.parent)
        Category.cache_display_delete()

        if is_display_old or category.is_display:
            cache_filter_update_web_delete()
            cache_filter_update_dashboard_delete()

        Log.push(
            None, 'CATEGORY', 'UPDATE', request.user, 'Update Category',
            status.HTTP_201_CREATED, note='category/dashboard/views.py update()',
            content_type=settings.CONTENT_TYPE('category.category'), content_id=serializer.data['id'],
            data_old=old_data, data_new=Category.get_log(category), data_change=data
        )
        return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     total = MyCart.objects.filter('total').first()
    #     if total == 0:
    #         total += total.get_food_menu
    #         return total
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)
    #
    # def perform_update(self, serializer):
    #     serializer.save()
    #
    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)

# @action(methods=['PATCH'], detail=False)
#    def update_approval_status(self, request, *args, **kwargs):
#        serializer = self.get_serializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        data = serializer.validated_data
#        approve_list = Approve.filter_list_by_status(
#            settings.CONTENT_TYPE('exam.slot'),
#            data['content_id_list']
#        )
#        approve_list.update(status=data['approval_status'], approve_account=request.user)
#        if data['approval_status'] == 1:
#            is_active = True
#        else:
#            is_active = False
#        Slot.objects.filter(
#            id__in=approve_list.values_list('content_id', flat=True)
#        ).update(is_active=is_active)
#        exam_name_list = []
#        for approve in approve_list:
#            slot = Slot.objects.select_related('section').filter(id=approve.content_id).first()
#            if slot:
#                exam = slot.section.exam
#                exam.update_score_and_count()
#                exam_name_list.append(exam.name)
#                slot.section.update_count_question()
#            approve.delete_cache()
#
#        Log.push(
#            None, 'BANK', 'APPROVE_REJECT_USAGE', request.user, 'Approve/Reject Usage',
#            status.HTTP_200_OK, content_type=settings.CONTENT_TYPE('bank.bank'), content_id=self.bank.id,
#            note='bank/dashboard/views_usage.py update_approval_status()',
#            data_new={
#                'exam_list': exam_name_list,
#                'status': approve_list.first().status_label
#            }
#        )
#        return Response()
