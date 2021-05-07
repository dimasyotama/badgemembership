from django.shortcuts import render
from badge_membership.models import PromoCode,Toko,BadgeName,MemberPrivilege,Profile
from badge_membership.serializers import TokoSerializers,PromoCode,ProfileSerializer,BadgeSerializers,MemberPrivilegeSerializer
from rest_framework.response import Response
from rest_framework import viewsets,generics


class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Toko.objects.all()
    serializer_class = TokoSerializers

    def get_queryset(self):
        queryset = self.queryset
        return queryset
    
    def details(self,request,pk=None):
        filter_by_id = Toko.objects.get(pk=pk)
        if filter_by_id is not None:
            queryset = filter_by_id
            serializer = TokoSerializers(queryset,many=False)
            return Response(serializer.data)
        else:
            return Response({"404":"Not Found"})

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
    
class GetBadgeViewSet(viewsets.ModelViewSet):
    gettting_badge = BadgeName.objects.all().values_list("nama_badge", flat=True)
    serializer_class = ProfileSerializer
    def get_badge(self,request,pk=None):
        queryset = self.gettting_badge
        profile = Profile.objects.get(pk=pk)
        if profile.freq_shop_user >= 200:
            profile.badge_name.add(getting_badge[0])
        elif profile.freq_shop_user >=300:
            profile.badge_name.add(getting_badge[1])
        elif profile.freq_shop_user >=400:
            profile.badge_name.add(getting_badge[2])
        elif profile.freq_shop_user >=500:
            profile.badge_name.add(getting_badge[3])
        else:
            profile.badge_name.add(getting_badge[4])

