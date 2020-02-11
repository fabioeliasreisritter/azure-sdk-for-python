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

from .thing_py3 import Thing


class CreativeWork(Thing):
    """The most generic kind of creative work, including books, movies,
    photographs, software programs, etc.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Action

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar potential_action:
    :vartype potential_action:
     list[~azure.cognitiveservices.search.autosuggest.models.Action]
    :ivar immediate_action:
    :vartype immediate_action:
     list[~azure.cognitiveservices.search.autosuggest.models.Action]
    :ivar preferred_clickthrough_url:
    :vartype preferred_clickthrough_url: str
    :ivar adaptive_card:
    :vartype adaptive_card: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar about: For internal use only.
    :vartype about:
     list[~azure.cognitiveservices.search.autosuggest.models.Thing]
    :ivar mentions: For internal use only.
    :vartype mentions:
     list[~azure.cognitiveservices.search.autosuggest.models.Thing]
    :ivar provider: The source of the creative work.
    :vartype provider:
     list[~azure.cognitiveservices.search.autosuggest.models.Thing]
    :ivar creator:
    :vartype creator: ~azure.cognitiveservices.search.autosuggest.models.Thing
    :ivar text: Text content of this creative work
    :vartype text: str
    :ivar discussion_url:
    :vartype discussion_url: str
    :ivar comment_count:
    :vartype comment_count: int
    :ivar main_entity:
    :vartype main_entity:
     ~azure.cognitiveservices.search.autosuggest.models.Thing
    :ivar head_line:
    :vartype head_line: str
    :ivar copyright_holder:
    :vartype copyright_holder:
     ~azure.cognitiveservices.search.autosuggest.models.Thing
    :ivar copyright_year:
    :vartype copyright_year: int
    :ivar disclaimer:
    :vartype disclaimer: str
    :ivar is_accessible_for_free:
    :vartype is_accessible_for_free: bool
    :ivar genre:
    :vartype genre: list[str]
    :ivar is_family_friendly:
    :vartype is_family_friendly: bool
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'potential_action': {'readonly': True},
        'immediate_action': {'readonly': True},
        'preferred_clickthrough_url': {'readonly': True},
        'adaptive_card': {'readonly': True},
        'url': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'about': {'readonly': True},
        'mentions': {'readonly': True},
        'provider': {'readonly': True},
        'creator': {'readonly': True},
        'text': {'readonly': True},
        'discussion_url': {'readonly': True},
        'comment_count': {'readonly': True},
        'main_entity': {'readonly': True},
        'head_line': {'readonly': True},
        'copyright_holder': {'readonly': True},
        'copyright_year': {'readonly': True},
        'disclaimer': {'readonly': True},
        'is_accessible_for_free': {'readonly': True},
        'genre': {'readonly': True},
        'is_family_friendly': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'potential_action': {'key': 'potentialAction', 'type': '[Action]'},
        'immediate_action': {'key': 'immediateAction', 'type': '[Action]'},
        'preferred_clickthrough_url': {'key': 'preferredClickthroughUrl', 'type': 'str'},
        'adaptive_card': {'key': 'adaptiveCard', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'about': {'key': 'about', 'type': '[Thing]'},
        'mentions': {'key': 'mentions', 'type': '[Thing]'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'creator': {'key': 'creator', 'type': 'Thing'},
        'text': {'key': 'text', 'type': 'str'},
        'discussion_url': {'key': 'discussionUrl', 'type': 'str'},
        'comment_count': {'key': 'commentCount', 'type': 'int'},
        'main_entity': {'key': 'mainEntity', 'type': 'Thing'},
        'head_line': {'key': 'headLine', 'type': 'str'},
        'copyright_holder': {'key': 'copyrightHolder', 'type': 'Thing'},
        'copyright_year': {'key': 'copyrightYear', 'type': 'int'},
        'disclaimer': {'key': 'disclaimer', 'type': 'str'},
        'is_accessible_for_free': {'key': 'isAccessibleForFree', 'type': 'bool'},
        'genre': {'key': 'genre', 'type': '[str]'},
        'is_family_friendly': {'key': 'isFamilyFriendly', 'type': 'bool'},
    }

    _subtype_map = {
        '_type': {'Action': 'Action'}
    }

    def __init__(self, **kwargs) -> None:
        super(CreativeWork, self).__init__(**kwargs)
        self.thumbnail_url = None
        self.about = None
        self.mentions = None
        self.provider = None
        self.creator = None
        self.text = None
        self.discussion_url = None
        self.comment_count = None
        self.main_entity = None
        self.head_line = None
        self.copyright_holder = None
        self.copyright_year = None
        self.disclaimer = None
        self.is_accessible_for_free = None
        self.genre = None
        self.is_family_friendly = None
        self._type = 'CreativeWork'