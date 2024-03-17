from datetime import date

from django_filters import rest_framework as dj_filters

from shop.models import Client


class CharInFilter(dj_filters.BaseInFilter, dj_filters.CharFilter):
    pass


class ClientFilter(dj_filters.FilterSet):
    age = dj_filters.NumberFilter(method='filter_by_age')
    age_range = dj_filters.RangeFilter(method='filter_by_age_range')

    class Meta:
        model = Client
        fields = ('category', 'gender', 'age', )

    def filter_by_age(self, queryset, name, value):
        today = date.today()
        birth_year_ago = today.year - int(value)
        birth_date_lower_bound = date(birth_year_ago, today.month, today.day)
        birth_date_upper_bound = date(birth_year_ago - 1, today.month, today.day)

        return queryset.filter(
            birth_ate__lte=birth_date_lower_bound,
            birth_ate__gte=birth_date_upper_bound
        )

    def filter_by_age_range(self, queryset, name, value):
        age_min, age_max = value.start, value.stop
        today = date.today()
        birth_min_year_ago = today.year - int(age_max)
        birth_max_year_ago = today.year - int(age_min)
        birth_min_date = date(birth_min_year_ago, today.month, today.day)
        birth_max_date = date(birth_max_year_ago, today.month, today.day)

        return queryset.filter(
            birth_ate__gte=birth_min_date,
            birth_ate__lte=birth_max_date
        )
