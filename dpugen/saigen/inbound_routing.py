#!/usr/bin/python3

import os

from saigen.confbase import *
from saigen.confutils import *

TEMPLATE_INBOUND_ROUTE = {
    'name': 'inbound_routing_#%(ENI)d',
    'op': 'create',
    'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
    'key': {
        'switch_id': '$SWITCH_ID',
        'eni_id': '%(ENI)d',
        'vni': '%(ENI)d'
    },
    'attributes': [
        'SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION',
        'SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP_PA_VALIDATE',
        'SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID',
        '$vnet_#%(ENI)d'
    ]
}


class InboundRouting(ConfBase):

    def __init__(self, params={}):
        super().__init__(params)

    def items(self):
        print('  Generating %s ...' % os.path.basename(__file__))
        self.num_yields = 0
        p = self.params

        for eni_index, eni in enumerate(range(p.ENI_START, p.ENI_START + p.ENI_COUNT * p.ENI_STEP, p.ENI_STEP)):
            self.num_yields += 1
            yield TEMPLATE_INBOUND_ROUTE % {
                'ENI':  eni
            }


if __name__ == '__main__':
    conf = InboundRouting()
    common_main(conf)
