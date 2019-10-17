from rest_framework import serializers

from mangequeue.models import Queue


class QueueSerializer(serializers.ModelSerializer):
    count_queue = serializers.SerializerMethodField()

    class Meta:
        model = Queue
        fields = ('table_number', 'queue', 'id')

    def count_queue(self, queue):
        return queue.count
