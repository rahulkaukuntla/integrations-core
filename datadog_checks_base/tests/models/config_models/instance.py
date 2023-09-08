# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, deprecations, validators


class Obj(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    bar: Optional[tuple[str, ...]] = None
    foo: bool


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    array: Optional[tuple[str, ...]] = None
    deprecated: Optional[str] = None
    flag: Optional[bool] = None
    hyphenated_name: Optional[str] = Field(None, alias='hyphenated-name')
    mapping: Optional[MappingProxyType[str, Any]] = None
    obj: Optional[Obj] = None
    pass_: Optional[str] = Field(None, alias='pass')
    pid: Optional[int] = None
    text: Optional[str] = None
    timeout: Optional[float] = None

    @model_validator(mode='before')
    def _handle_deprecations(cls, values, info):
        fields = info.context['configured_fields']
        validation.utils.handle_deprecations('instances', deprecations.instance(), fields, info.context)
        return values

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
