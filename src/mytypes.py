import collections

InstanceType = collections.namedtuple(
    'InstanceType',
    [
        'size',
        'availability_zone',
        'tenancy',
        'product',
        'vpc'
    ]
)

InstanceReservation = collections.namedtuple(
    'InstanceReservation',
    [
        'type',
        'cost_hourly',
        'cost_upfront',
        'count',
    ]
)

InstanceOffering = collections.namedtuple(
    'InstanceOffering',
    [
        'type',
        'cost_ondemand',
        'cost_reserved_worst',
        'cost_reserved_best',
    ]
)

InstanceMatching = collections.namedtuple(
    'InstanceMatching',
    [
        'offering',
        'count_reserved',
        'count',
    ]
)
