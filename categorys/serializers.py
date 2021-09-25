from rest_framework import serializers
from .models import Category, Branch, Contact, Course


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'latitude', 'longitude', 'address', 'course')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'status', 'value', 'course')


class CourseSerializer(serializers.ModelSerializer):
    contact1 = ContactSerializer(many=True, read_only=True)
    branch1 = BranchSerializer(many=True, read_only=True)
    category1 = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'logo', 'contact1', 'branch1', 'category1')

    def create(self, validated_data):
        category_data = validated_data.pop('category1')
        category = Category.objects.create(**category_data)
        contacts_data = validated_data.pop('contact1')
        branches_data = validated_data.pop('branch1')
        courses = Course.objects.create(category=category, **validated_data)
        contacts_list = []
        branches_list = []
        for contact in contacts_data:
            contact_id = contact.pop('id', None)
            contact, _ = Contact.objects.get_or_create(id=contact_id, defaults=contact)
            contacts_list.append(contact)
        for branch in branches_data:
            branch_id = branch.pop('id', None)
            branch, _ = Branch.objects.get_or_create(id=branch_id, defaults=branch)
            branches_list.append(branch)
        courses.contacts.add(*contacts_list)
        courses.branches.add(*branches_list)
        return courses
