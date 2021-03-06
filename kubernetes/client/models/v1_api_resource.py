# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1APIResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, kind=None, name=None, namespaced=None, short_names=None, verbs=None):
        """
        V1APIResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'name': 'str',
            'namespaced': 'bool',
            'short_names': 'list[str]',
            'verbs': 'list[str]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'name': 'name',
            'namespaced': 'namespaced',
            'short_names': 'shortNames',
            'verbs': 'verbs'
        }

        self._kind = kind
        self._name = name
        self._namespaced = namespaced
        self._short_names = short_names
        self._verbs = verbs

    @property
    def kind(self):
        """
        Gets the kind of this V1APIResource.
        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')

        :return: The kind of this V1APIResource.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1APIResource.
        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')

        :param kind: The kind of this V1APIResource.
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1APIResource.
        name is the name of the resource.

        :return: The name of this V1APIResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1APIResource.
        name is the name of the resource.

        :param name: The name of this V1APIResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def namespaced(self):
        """
        Gets the namespaced of this V1APIResource.
        namespaced indicates if a resource is namespaced or not.

        :return: The namespaced of this V1APIResource.
        :rtype: bool
        """
        return self._namespaced

    @namespaced.setter
    def namespaced(self, namespaced):
        """
        Sets the namespaced of this V1APIResource.
        namespaced indicates if a resource is namespaced or not.

        :param namespaced: The namespaced of this V1APIResource.
        :type: bool
        """
        if namespaced is None:
            raise ValueError("Invalid value for `namespaced`, must not be `None`")

        self._namespaced = namespaced

    @property
    def short_names(self):
        """
        Gets the short_names of this V1APIResource.
        shortNames is a list of suggested short names of the resource.

        :return: The short_names of this V1APIResource.
        :rtype: list[str]
        """
        return self._short_names

    @short_names.setter
    def short_names(self, short_names):
        """
        Sets the short_names of this V1APIResource.
        shortNames is a list of suggested short names of the resource.

        :param short_names: The short_names of this V1APIResource.
        :type: list[str]
        """

        self._short_names = short_names

    @property
    def verbs(self):
        """
        Gets the verbs of this V1APIResource.
        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)

        :return: The verbs of this V1APIResource.
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """
        Sets the verbs of this V1APIResource.
        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)

        :param verbs: The verbs of this V1APIResource.
        :type: list[str]
        """
        if verbs is None:
            raise ValueError("Invalid value for `verbs`, must not be `None`")

        self._verbs = verbs

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
