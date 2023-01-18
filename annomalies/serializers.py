from rest_framework import serializers
from annomalies import models
import collections


class parcelValidator:
    conditioner_required_fields=[]
    def validate(self, attrs):
        for item in self.conditioner_required_fields:

            for master_field, conditions in item.items():
                condition_name=master_field
                master_field=attrs.get(master_field)
                trigger=master_field==conditions['condition']
                condition=conditions['condition']
                if trigger:
                    for key, value in conditions['required_fields'].items():
                        if attrs.get(key)==value:
                            raise serializers.ValidationError('%s Cannot be %s if %s is %s'% (condition_name,condition,key, value))
                        

        return attrs
class issuesSerializer(parcelValidator, serializers.ModelSerializer):
    
    class Meta:
        model= models.issues
        # exclude=['id']
        fields = '__all__'

class parcelSerializer(parcelValidator, serializers.ModelSerializer):
    conditioner_required_fields=[{ 
        'waterfall':{
            'condition':True,
            'required_fields':{
                'tenure':False,
                'ownership':False,
                'registered':False

            }
        }
    },
    { 
        'tenure':{
            'condition':True,
            'required_fields':{
                'land_admin_parcel_status':False

            }
        }
    },

    { 
        'ownership':{
            'condition':True,
            'required_fields':{
                'land_reg_status':False,
                'registered':False

            }
        }
    }
    ]
    class Meta:
        model= models.parcel
        exclude=['id']

class issueDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.issue_details
        fields='__all__'


            