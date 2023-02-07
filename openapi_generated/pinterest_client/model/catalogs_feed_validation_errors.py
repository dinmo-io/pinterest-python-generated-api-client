"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.8.0
    Contact: pinterest-api@pinterest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_generated.pinterest_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_generated.pinterest_client.exceptions import ApiAttributeError



class CatalogsFeedValidationErrors(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'fetch_error': (int,),  # noqa: E501
            'fetch_inactive_feed_error': (int,),  # noqa: E501
            'encoding_error': (int,),  # noqa: E501
            'delimiter_error': (int,),  # noqa: E501
            'required_columns_missing': (int,),  # noqa: E501
            'image_link_invalid': (int,),  # noqa: E501
            'itemid_missing': (int,),  # noqa: E501
            'title_missing': (int,),  # noqa: E501
            'description_missing': (int,),  # noqa: E501
            'product_link_missing': (int,),  # noqa: E501
            'image_link_missing': (int,),  # noqa: E501
            'availability_invalid': (int,),  # noqa: E501
            'product_price_invalid': (int,),  # noqa: E501
            'link_format_invalid': (int,),  # noqa: E501
            'parse_line_error': (int,),  # noqa: E501
            'adwords_format_invalid': (int,),  # noqa: E501
            'internal_service_error': (int,),  # noqa: E501
            'no_verified_domain': (int,),  # noqa: E501
            'adult_invalid': (int,),  # noqa: E501
            'image_link_length_too_long': (int,),  # noqa: E501
            'invalid_domain': (int,),  # noqa: E501
            'feed_length_too_long': (int,),  # noqa: E501
            'link_length_too_long': (int,),  # noqa: E501
            'malformed_xml': (int,),  # noqa: E501
            'price_missing': (int,),  # noqa: E501
            'feed_too_small': (int,),  # noqa: E501
            'max_items_per_item_group_exceeded': (int,),  # noqa: E501
            'item_main_image_download_failure': (int,),  # noqa: E501
            'pinjoin_content_unsafe': (int,),  # noqa: E501
            'blocklisted_image_signature': (int,),  # noqa: E501
            'list_price_invalid': (int,),  # noqa: E501
            'price_cannot_be_determined': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fetch_error': 'FETCH_ERROR',  # noqa: E501
        'fetch_inactive_feed_error': 'FETCH_INACTIVE_FEED_ERROR',  # noqa: E501
        'encoding_error': 'ENCODING_ERROR',  # noqa: E501
        'delimiter_error': 'DELIMITER_ERROR',  # noqa: E501
        'required_columns_missing': 'REQUIRED_COLUMNS_MISSING',  # noqa: E501
        'image_link_invalid': 'IMAGE_LINK_INVALID',  # noqa: E501
        'itemid_missing': 'ITEMID_MISSING',  # noqa: E501
        'title_missing': 'TITLE_MISSING',  # noqa: E501
        'description_missing': 'DESCRIPTION_MISSING',  # noqa: E501
        'product_link_missing': 'PRODUCT_LINK_MISSING',  # noqa: E501
        'image_link_missing': 'IMAGE_LINK_MISSING',  # noqa: E501
        'availability_invalid': 'AVAILABILITY_INVALID',  # noqa: E501
        'product_price_invalid': 'PRODUCT_PRICE_INVALID',  # noqa: E501
        'link_format_invalid': 'LINK_FORMAT_INVALID',  # noqa: E501
        'parse_line_error': 'PARSE_LINE_ERROR',  # noqa: E501
        'adwords_format_invalid': 'ADWORDS_FORMAT_INVALID',  # noqa: E501
        'internal_service_error': 'INTERNAL_SERVICE_ERROR',  # noqa: E501
        'no_verified_domain': 'NO_VERIFIED_DOMAIN',  # noqa: E501
        'adult_invalid': 'ADULT_INVALID',  # noqa: E501
        'image_link_length_too_long': 'IMAGE_LINK_LENGTH_TOO_LONG',  # noqa: E501
        'invalid_domain': 'INVALID_DOMAIN',  # noqa: E501
        'feed_length_too_long': 'FEED_LENGTH_TOO_LONG',  # noqa: E501
        'link_length_too_long': 'LINK_LENGTH_TOO_LONG',  # noqa: E501
        'malformed_xml': 'MALFORMED_XML',  # noqa: E501
        'price_missing': 'PRICE_MISSING',  # noqa: E501
        'feed_too_small': 'FEED_TOO_SMALL',  # noqa: E501
        'max_items_per_item_group_exceeded': 'MAX_ITEMS_PER_ITEM_GROUP_EXCEEDED',  # noqa: E501
        'item_main_image_download_failure': 'ITEM_MAIN_IMAGE_DOWNLOAD_FAILURE',  # noqa: E501
        'pinjoin_content_unsafe': 'PINJOIN_CONTENT_UNSAFE',  # noqa: E501
        'blocklisted_image_signature': 'BLOCKLISTED_IMAGE_SIGNATURE',  # noqa: E501
        'list_price_invalid': 'LIST_PRICE_INVALID',  # noqa: E501
        'price_cannot_be_determined': 'PRICE_CANNOT_BE_DETERMINED',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CatalogsFeedValidationErrors - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            fetch_error (int): Pinterest couldn't download your feed.. [optional]  # noqa: E501
            fetch_inactive_feed_error (int): Your feed wasn't ingested because it hasn’t changed in the previous 90 days.. [optional]  # noqa: E501
            encoding_error (int): Your feed includes data with an unsupported encoding format.. [optional]  # noqa: E501
            delimiter_error (int): Your feed includes data with formatting errors.. [optional]  # noqa: E501
            required_columns_missing (int): Your feed is missing some required column headers.. [optional]  # noqa: E501
            image_link_invalid (int): Some image links are formatted incorrectly.. [optional]  # noqa: E501
            itemid_missing (int): Some items are missing an item id in their product metadata, those items will not be published.. [optional]  # noqa: E501
            title_missing (int): Some items are missing a title in their product metadata, those items will not be published.. [optional]  # noqa: E501
            description_missing (int): Some items are missing a description in their product metadata, those items will not be published.. [optional]  # noqa: E501
            product_link_missing (int): Some items are missing a link URL in their product metadata, those items will not be published.. [optional]  # noqa: E501
            image_link_missing (int): Some items are missing an image link URL in their product metadata, those items will not be published.. [optional]  # noqa: E501
            availability_invalid (int): Some items are missing an availability value in their product metadata, those items will not be published.. [optional]  # noqa: E501
            product_price_invalid (int): Some items have price formatting errors in their product metadata, those items will not be published.. [optional]  # noqa: E501
            link_format_invalid (int): Some link values are formatted incorrectly.. [optional]  # noqa: E501
            parse_line_error (int): Your feed contains formatting errors for some items.. [optional]  # noqa: E501
            adwords_format_invalid (int): Some adwords links contain too many characters.. [optional]  # noqa: E501
            internal_service_error (int): We experienced a technical difficulty and were unable to ingest your feed. The next ingestion will happen in 24 hours.. [optional]  # noqa: E501
            no_verified_domain (int): Your merchant domain needs to be claimed.. [optional]  # noqa: E501
            adult_invalid (int): Some items have invalid adult values.. [optional]  # noqa: E501
            image_link_length_too_long (int): Some items have image_link URLs that contain too many characters, so those items will not be published.. [optional]  # noqa: E501
            invalid_domain (int): Some of your product link values don't match the verified domain associated with this account.. [optional]  # noqa: E501
            feed_length_too_long (int): Your feed contains too many items, some items will not be published.. [optional]  # noqa: E501
            link_length_too_long (int): Some product links contain too many characters, those items will not be published.. [optional]  # noqa: E501
            malformed_xml (int): Your feed couldn't be validated because the xml file is formatted incorrectly.. [optional]  # noqa: E501
            price_missing (int): Some products are missing a price, those items will not be published.. [optional]  # noqa: E501
            feed_too_small (int): Your feed couldn't be validated because the file doesn't contain the minimum number of lines required.. [optional]  # noqa: E501
            max_items_per_item_group_exceeded (int): Some items exceed the maximum number of items per item group, those items will not be published.. [optional]  # noqa: E501
            item_main_image_download_failure (int): Some items' main images can't be found.. [optional]  # noqa: E501
            pinjoin_content_unsafe (int): Some items were not published because they don't meet Pinterest's Merchant Guidelines.. [optional]  # noqa: E501
            blocklisted_image_signature (int): Some items were not published because they don't meet Pinterest's Merchant Guidelines.. [optional]  # noqa: E501
            list_price_invalid (int): Some items have list price formatting errors in their product metadata, those items will not be published.. [optional]  # noqa: E501
            price_cannot_be_determined (int): Some items were not published because price cannot be determined. The price, list price, and sale price are all different, so those items will not be published.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """CatalogsFeedValidationErrors - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            fetch_error (int): Pinterest couldn't download your feed.. [optional]  # noqa: E501
            fetch_inactive_feed_error (int): Your feed wasn't ingested because it hasn’t changed in the previous 90 days.. [optional]  # noqa: E501
            encoding_error (int): Your feed includes data with an unsupported encoding format.. [optional]  # noqa: E501
            delimiter_error (int): Your feed includes data with formatting errors.. [optional]  # noqa: E501
            required_columns_missing (int): Your feed is missing some required column headers.. [optional]  # noqa: E501
            image_link_invalid (int): Some image links are formatted incorrectly.. [optional]  # noqa: E501
            itemid_missing (int): Some items are missing an item id in their product metadata, those items will not be published.. [optional]  # noqa: E501
            title_missing (int): Some items are missing a title in their product metadata, those items will not be published.. [optional]  # noqa: E501
            description_missing (int): Some items are missing a description in their product metadata, those items will not be published.. [optional]  # noqa: E501
            product_link_missing (int): Some items are missing a link URL in their product metadata, those items will not be published.. [optional]  # noqa: E501
            image_link_missing (int): Some items are missing an image link URL in their product metadata, those items will not be published.. [optional]  # noqa: E501
            availability_invalid (int): Some items are missing an availability value in their product metadata, those items will not be published.. [optional]  # noqa: E501
            product_price_invalid (int): Some items have price formatting errors in their product metadata, those items will not be published.. [optional]  # noqa: E501
            link_format_invalid (int): Some link values are formatted incorrectly.. [optional]  # noqa: E501
            parse_line_error (int): Your feed contains formatting errors for some items.. [optional]  # noqa: E501
            adwords_format_invalid (int): Some adwords links contain too many characters.. [optional]  # noqa: E501
            internal_service_error (int): We experienced a technical difficulty and were unable to ingest your feed. The next ingestion will happen in 24 hours.. [optional]  # noqa: E501
            no_verified_domain (int): Your merchant domain needs to be claimed.. [optional]  # noqa: E501
            adult_invalid (int): Some items have invalid adult values.. [optional]  # noqa: E501
            image_link_length_too_long (int): Some items have image_link URLs that contain too many characters, so those items will not be published.. [optional]  # noqa: E501
            invalid_domain (int): Some of your product link values don't match the verified domain associated with this account.. [optional]  # noqa: E501
            feed_length_too_long (int): Your feed contains too many items, some items will not be published.. [optional]  # noqa: E501
            link_length_too_long (int): Some product links contain too many characters, those items will not be published.. [optional]  # noqa: E501
            malformed_xml (int): Your feed couldn't be validated because the xml file is formatted incorrectly.. [optional]  # noqa: E501
            price_missing (int): Some products are missing a price, those items will not be published.. [optional]  # noqa: E501
            feed_too_small (int): Your feed couldn't be validated because the file doesn't contain the minimum number of lines required.. [optional]  # noqa: E501
            max_items_per_item_group_exceeded (int): Some items exceed the maximum number of items per item group, those items will not be published.. [optional]  # noqa: E501
            item_main_image_download_failure (int): Some items' main images can't be found.. [optional]  # noqa: E501
            pinjoin_content_unsafe (int): Some items were not published because they don't meet Pinterest's Merchant Guidelines.. [optional]  # noqa: E501
            blocklisted_image_signature (int): Some items were not published because they don't meet Pinterest's Merchant Guidelines.. [optional]  # noqa: E501
            list_price_invalid (int): Some items have list price formatting errors in their product metadata, those items will not be published.. [optional]  # noqa: E501
            price_cannot_be_determined (int): Some items were not published because price cannot be determined. The price, list price, and sale price are all different, so those items will not be published.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
