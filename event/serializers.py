from rest_framework import serializers
from .models import Event, Show, Showtype, Genre, File

from general.serializers import CitySerializer


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class ShowTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showtype
        fields = '__all__'


class ShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Show
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['showtypeid'] = '' if instance.showtypeid == "" or instance.showtypeid is None else ShowTypeSerializer(
            instance.showtypeid).data
        response['genreid'] = '' if instance.genreid == "" or instance.genreid is None else GenreSerializer(
            instance.genreid).data
        response['files'] = '' if instance.file_set == "" or instance.file_set is None else FileSerializer(
            instance.file_set, many=True).data

        return response


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'local', 'schedule', 'showid', 'presentationdate', )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['showid'] = '' if instance.showid == "" or instance.showid is None else {
            'name': instance.showid.name,
            'files': '' if instance.showid.file_set == "" or instance.showid.file_set is None else FileSerializer(
                instance.showid.file_set, many=True).data
        }
        response['cityid'] = '' if instance.cityid == "" or instance.cityid is None else CitySerializer(
            instance.cityid).data
        return response


class EventDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['showid'] = '' if instance.showid == "" or instance.showid is None else ShowSerializer(
            instance.showid).data
        response['cityid'] = '' if instance.cityid == "" or instance.cityid is None else CitySerializer(
            instance.cityid).data
        return response
