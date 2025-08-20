# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2022 TU Wien.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Schemas for user profiles and preferences."""

import pytz
from flask import current_app
from invenio_i18n import lazy_gettext as _
from marshmallow import Schema, ValidationError, fields


def validate_visibility(value):
    """Check if the value is a valid visibility setting."""
    if value not in ["public", "restricted"]:
        raise ValidationError(
            message=str(_("Value must be either 'public' or 'restricted'."))
        )


def validate_locale(value):
    """Check if the value is a valid locale."""
    locales = current_app.extensions["invenio-i18n"].get_locales()
    locales = [locale.language for locale in locales]

    if value not in locales:
        raise ValidationError(message=str(_("Value must be a valid locale.")))
    current_app.config["BABEL_DEFAULT_LOCALE"] = value


def validate_timezone(value):
    """Check if the value is a valid timezone."""
    if value not in pytz.all_timezones:
        raise ValidationError(message=str(_("Value must be a valid timezone.")))
    current_app.config["BABEL_DEFAULT_TIMEZONE"] = value


class UserProfileSchema(Schema):
    """The default user profile schema."""
    # default invenio fields
    full_name = fields.String()
    affiliations = fields.String()
    email = fields.String()

    # profile main tabs
    given_name = fields.String()
    affiliation_to_entities = fields.String()
    family_name = fields.String()

    orcid = fields.String()
    linkedin = fields.String()

    gender = fields.String()
    university = fields.String()
    profile_links = fields.String()
    languages =  fields.String()
    expert_profile =  fields.String()
    faculty_center_institute =  fields.String()
    department =  fields.String()
    career_stage =  fields.String()
    others_initiatives = fields.String()
    research_group_member =  fields.Boolean()
    additional_keywords =  fields.String()
    areas_of_expertise =  fields.String()
    main_keywords =  fields.String()
    trl_level =  fields.String()
    principal_investigator  =  fields.String()
    research_group_pi =  fields.Boolean()

    # profile projects tabs
    eu_proposal_writer = fields.Boolean()
    eu_project_leader = fields.Boolean()
    eu_project_member = fields.Boolean()
    eu_project_evaluator = fields.Boolean()
    knowledge_transfer = fields.Boolean()
    coordinated_projects_and_calls = fields.String()
    profile_please_indicate_the_full_name_of_your_research_group_in_english = fields.String()
    founder_of_a_spin_off = fields.Boolean()
    member_of_a_spin_off= fields.Boolean()
    patents= fields.Boolean()
    member_of_an_industrial_chair= fields.Boolean()
    projects_other = fields.Boolean()
    projects_other_response= fields.String()
    projects_affiliated_relevant_associations_platforms_clusters = fields.String()

    # profile research_groups tabs
    interest_in_joint_research_groups = fields.Boolean()
    relevant_publications = fields.String()
    relevant_projects = fields.String()

    # profile consent tabs
    consent_by_providing_my_consent= fields.Boolean()
    visibility= fields.Boolean()

class UserPreferencesSchema(Schema):
    """The default schema for user preferences."""

    visibility = fields.String(validate=validate_visibility)
    email_visibility = fields.String(validate=validate_visibility)
    locale = fields.String(validate=validate_locale)
    timezone = fields.String(validate=validate_timezone)
