from rest_framework.pagination import LimitOffsetPagination as DRFPagination
from collections import OrderedDict


class LimitOffsetPagination(DRFPagination):
    default_limit = 10

    def paginate(self, request, queryset):
        limit = self.get_limit(request) or self.default_limit
        offset = self.get_offset(request)
        count = self.get_count(queryset)
        return queryset[offset:offset + limit], count

    def get_paginated_response(self, data):
        return OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ])