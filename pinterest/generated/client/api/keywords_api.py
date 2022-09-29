"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.5.0
    Contact: pinterest-api@pinterest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pinterest.generated.client.api_client import ApiClient, Endpoint as _Endpoint
from pinterest.generated.client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.keyword_update_body import KeywordUpdateBody
from pinterest.generated.client.model.keywords_request import KeywordsRequest
from pinterest.generated.client.model.keywords_response import KeywordsResponse
from pinterest.generated.client.model.match_type import MatchType
from pinterest.generated.client.model.paginated import Paginated


class KeywordsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.keywords_create_endpoint = _Endpoint(
            settings={
                'response_type': (KeywordsResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/keywords',
                'operation_id': 'keywords_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'keywords_request',
                ],
                'required': [
                    'ad_account_id',
                    'keywords_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 19,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'keywords_request':
                        (KeywordsRequest,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'keywords_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.keywords_get_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/keywords',
                'operation_id': 'keywords_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'campaign_id',
                    'ad_group_id',
                    'match_types',
                    'page_size',
                    'bookmark',
                ],
                'required': [
                    'ad_account_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                    'campaign_id',
                    'match_types',
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 19,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                    ('campaign_id',): {

                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                    ('match_types',): {

                        'max_items': 5,
                        'min_items': 1,
                    },
                    ('page_size',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'campaign_id':
                        (str,),
                    'ad_group_id':
                        (str,),
                    'match_types':
                        ([MatchType],),
                    'page_size':
                        (int,),
                    'bookmark':
                        (str,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'campaign_id': 'campaign_id',
                    'ad_group_id': 'ad_group_id',
                    'match_types': 'match_types',
                    'page_size': 'page_size',
                    'bookmark': 'bookmark',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'campaign_id': 'query',
                    'ad_group_id': 'query',
                    'match_types': 'query',
                    'page_size': 'query',
                    'bookmark': 'query',
                },
                'collection_format_map': {
                    'match_types': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.keywords_update_endpoint = _Endpoint(
            settings={
                'response_type': (KeywordsResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/keywords',
                'operation_id': 'keywords_update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'keyword_update_body',
                ],
                'required': [
                    'ad_account_id',
                    'keyword_update_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 19,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'keyword_update_body':
                        (KeywordUpdateBody,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'keyword_update_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def keywords_create(
        self,
        ad_account_id,
        keywords_request,
        **kwargs
    ):
        """Create keywords  # noqa: E501

        <strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> Create keywords.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.keywords_create(ad_account_id, keywords_request, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            keywords_request (KeywordsRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            KeywordsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        kwargs['keywords_request'] = \
            keywords_request
        return self.keywords_create_endpoint.call_with_http_info(**kwargs)

    def keywords_get(
        self,
        ad_account_id,
        **kwargs
    ):
        """Get keywords  # noqa: E501

        <strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> <p>Get a list of keywords based on the filters provided.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.keywords_get(ad_account_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.

        Keyword Args:
            campaign_id (str): Campaign Id to use to filter the results.. [optional]
            ad_group_id (str): Ad group Id.. [optional]
            match_types ([MatchType]): Keyword <a href=\"/docs/redoc/#section/Match-type-(keyword).\">match type</a>. [optional]
            page_size (int): Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information.. [optional] if omitted the server will use the default value of 25
            bookmark (str): Cursor used to fetch the next page of items. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        return self.keywords_get_endpoint.call_with_http_info(**kwargs)

    def keywords_update(
        self,
        ad_account_id,
        keyword_update_body,
        **kwargs
    ):
        """Update keywords  # noqa: E501

        <strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> <p>Update one or more keywords' bid and archived fields.</p> <p>Archiving a keyword effectively deletes it - keywords no longer receive metrics and no longer visible within the parent entity's keywords list.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.keywords_update(ad_account_id, keyword_update_body, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            keyword_update_body (KeywordUpdateBody):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            KeywordsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        kwargs['keyword_update_body'] = \
            keyword_update_body
        return self.keywords_update_endpoint.call_with_http_info(**kwargs)

