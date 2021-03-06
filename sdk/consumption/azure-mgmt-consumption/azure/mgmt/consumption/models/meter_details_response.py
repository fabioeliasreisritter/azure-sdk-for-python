# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterDetailsResponse(Model):
    """The properties of the meter detail.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar meter_name: The name of the meter, within the given meter category
    :vartype meter_name: str
    :ivar meter_category: The category of the meter, for example, 'Cloud
     services', 'Networking', etc..
    :vartype meter_category: str
    :ivar meter_sub_category: The subcategory of the meter, for example, 'A6
     Cloud services', 'ExpressRoute (IXP)', etc..
    :vartype meter_sub_category: str
    :ivar unit_of_measure: The unit in which the meter consumption is charged,
     for example, 'Hours', 'GB', etc.
    :vartype unit_of_measure: str
    :ivar service_family: The service family.
    :vartype service_family: str
    """

    _validation = {
        'meter_name': {'readonly': True},
        'meter_category': {'readonly': True},
        'meter_sub_category': {'readonly': True},
        'unit_of_measure': {'readonly': True},
        'service_family': {'readonly': True},
    }

    _attribute_map = {
        'meter_name': {'key': 'meterName', 'type': 'str'},
        'meter_category': {'key': 'meterCategory', 'type': 'str'},
        'meter_sub_category': {'key': 'meterSubCategory', 'type': 'str'},
        'unit_of_measure': {'key': 'unitOfMeasure', 'type': 'str'},
        'service_family': {'key': 'serviceFamily', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MeterDetailsResponse, self).__init__(**kwargs)
        self.meter_name = None
        self.meter_category = None
        self.meter_sub_category = None
        self.unit_of_measure = None
        self.service_family = None
