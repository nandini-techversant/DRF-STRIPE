from rest_framework import serializers

class StripePaymentSerializer(serializers.Serializer):
    amount = serializers.CharField(max_length=200)
    # currency = serializers.CharField(max_length=200)
    # automatic_payment_methods = serializers.BooleanField()

    class Meta:
        fields = ('amount')

        
    