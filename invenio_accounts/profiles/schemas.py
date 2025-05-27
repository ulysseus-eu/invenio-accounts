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
    
    # profile main tabs
    given_name = fields.String()
    Affiliation_to_entities = fields.String()
    family_name = fields.String()
    
    orcid = fields.String()
    linkedin = fields.String()
    
    Gender = fields.String()
    University = fields.String()
    profile_links = fields.String()
    Languages =  fields.String()
    Expert_profile =  fields.String()
    Faculty_Center_Institute =  fields.String()
    Department =  fields.String()
    Career_stage =  fields.String()
    Research_Group_member =  fields.Boolean()
    Additional_Keywords =  fields.String()
    Areas_of_expertise =  fields.String()
    Main_Keywords =  fields.String()
    TRL_level =  fields.String()
    Principal_Investigator  =  fields.String()
    Research_Group_PI =  fields.Boolean()
    
    # profile projects tabs
    projects_have_you_ever_designed_or_written_a_european_project_proposal = fields.Boolean()
    projects_have_you_ever_participated_in_a_granted_european_project_as_consortium_leader = fields.Boolean()
    projects_have_you_ever_participated_in_a_granted_european_project_as_a_member_of_consortium = fields.Boolean()
    projects_have_you_been_an_evaluator_of_eu_projects = fields.Boolean()
    projects_has_your_research_resulted_in_a_knowledge_transfer_initiative = fields.Boolean()
    projects_if_yes_please_name_the_project_s_you_have_coordinated_including_the_corresponding_call_s = fields.String()
    profile_please_indicate_the_full_name_of_your_research_group_in_english = fields.String()
    projects_i_have_founded_a_spin_off_company_as_a_result_of_my_research = fields.Boolean()
    projects_i_am_a_member_of_a_spin_off_company_linked_to_my_university= fields.Boolean()
    projects_i_have_patented_the_results_of_my_research= fields.Boolean()
    projects_i_am_an_active_member_of_a_business_chair_linked_to_my_university= fields.Boolean()
    projects_other = fields.Boolean()
    projects_other_response= fields.String()
    projects_affiliated_relevant_associations_platforms_clusters = fields.String()
    
    # profile research_groups tabs
    research_group_are_you_interested_in_participating_in_building_joint_research_groups_centered_around_shared_research_disciplines_within_ulysseus_partner_universities = fields.Boolean()
    research_group_most_relevant_to_your_research = fields.String()
    research_group_information_on_the_most_significant_projects = fields.String()
    
    # profile consent tabs
    consent_by_providing_my_consent= fields.Boolean()
    consent_profile_privacy_level= fields.Boolean()

class UserPreferencesSchema(Schema):
    """The default schema for user preferences."""

    visibility = fields.String(validate=validate_visibility)
    email_visibility = fields.String(validate=validate_visibility)
    locale = fields.String(validate=validate_locale)
    timezone = fields.String(validate=validate_timezone)
