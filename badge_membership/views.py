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


