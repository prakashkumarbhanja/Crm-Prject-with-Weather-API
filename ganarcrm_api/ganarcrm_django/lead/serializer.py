from statistics import mode
from rest_framework import serializers

from lead.models import *

from team.serializers import UserSerializer

class LeadSerializer(serializers.ModelSerializer):
    
    """
    Here test is a readonly field for demo and this is 
    How we can use ReadOnlyField( as a extra serialized field)

    """
    test = serializers.ReadOnlyField()

    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Lead
        fields = ['id',
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'assigned_to',
            'created_at',
            'modified_at',
            "test",
            ]

        read_only_fields = (
            'created_by',
            
        ),
            

