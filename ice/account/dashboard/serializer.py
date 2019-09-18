from rest_framework import serializers

from ice.account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    notification_count = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'notification_count'
        )

        def __init__(self, *args, **kwargs):
            # Don't pass the 'fields' arg up to the superclass
            fields = kwargs.pop('fields', None)

            # Instantiate the superclass normally
            super().__init__(*args, **kwargs)

            if fields is not None:
                # Drop any fields that are not specified in the `fields` argument.
                allowed = set(fields)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)


class AccountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'image',
            'supervisor',
        )


class AccountCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_null=True, required=False)
    level = serializers.IntegerField(required=False, allow_null=True)

    supervisor = serializers.IntegerField(required=False, allow_null=True)
    department = serializers.IntegerField(required=False, allow_null=True)
    position = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
            'is_force_reset_password',
            'phone',
            'level',
            'supervisor',
            'department',
            'position',
        )

    def validate_username(self, value):
        if Account.objects.filter(username=value).exists():
            raise serializers.ValidationError('A user with that username already exists.')
        return value

    def validate_email(self, value):
        if value is not None and Account.objects.filter(email=value).exists():
            raise serializers.ValidationError('selfA user with that email already exists.')
        return value