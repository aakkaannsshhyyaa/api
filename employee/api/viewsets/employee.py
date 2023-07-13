from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response
from rest_framework import viewsets


from employee.api.serializers.employee import EmployeeSerializer
from employee.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = [
        "post",
        "get",
        "patch",
    ]

    @extend_schema(
        summary="Refers to schemas at Bottom",
        description="Employee Create Api",
        request=EmployeeSerializer,
        responses={
            200: {
                "description": "Success message",
            },
            422: {
                "description": "Error message",
            },
        },
        tags=["Employee Apis"],
    )
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "title": "Employee",
                "message": "Created successfully",
                "data": response.data,
            }
        )

    @extend_schema(
        summary="Refers to schemas at Bottom",
        description="Employee Get Api",
        request=EmployeeSerializer,
        responses={
            200: {
                "description": "Success message",
            },
            422: {
                "description": "Error message",
            },
        },
        tags=["Employee Apis"],
    )
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            {
                "title": "Employee",
                "message": "Listed successfully",
                "data": response.data,
            }
        )

    @extend_schema(
        summary="Refers to schemas at Bottom",
        description="Employee Retrieve Api",
        request=EmployeeSerializer,
        responses={
            200: {
                "description": "Success message",
            },
            422: {
                "description": "Error message",
            },
        },
        tags=["Employee Apis"],
    )
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response(
            {
                "title": "Employee",
                "message": "Retrieved successfully",
                "data": response.data,
            }
        )

    @extend_schema(
        summary="Refers to schema at Bottom",
        description="Update Api",
        request=EmployeeSerializer,
        responses={
            200: {
                "description": "Success Message",
            },
            422: {
                "description": "Error message",
            },
        },
        tags=["Employee Apis"],
    )
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response(
            {
                "title": "Employee",
                "message": "Updated successfully",
            }
        )
