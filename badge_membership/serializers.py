from rest_framework import serializers
from badge_membership.models import PromoCode,Toko,BadgeName,MemberPrivilege,Profile

class TokoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Toko
        fields = '__all__'

class BadgeSerializers(serializers.ModelSerializer):
    class Meta:
        model = BadgeName
        fields = '__all__'

class PromoCodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    nama_produk = TokoSerializers()
    
    class Meta:
        model = Profile
        fields = ('nama','freq_shop_user','user','nama_produk')    
   

class MemberPrivilegeSerializer(serializers.ModelSerializer):
    code_promo = serializers.SerializerMethodField()
    freq_user_shop = serializers.SerializerMethodField()
    
    def get_code_promo(self,obj):
        dicts = []
        for obj in PromoCode.objects.filter(code_promo=obj.code_promo):
            data = dicts()
            data['code_promo'] = obj.code_promo
            data['discount_promo'] = obj.discount_promo
            

    class Meta:
        model = MemberPrivilege
        fields = "__all__"


    