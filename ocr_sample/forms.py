#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 Junction Applications
# Author: Aaron MacGillivary
# Project: pytesseract_django_sample

from django import forms


class UploadFileForm(forms.Form):
    """
    Simplest of forms to provide file upload
    """
    file_upload = forms.FileField()