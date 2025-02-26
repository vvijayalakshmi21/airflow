# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from airflow_breeze.utils.docker_command_utils import get_extra_docker_flags
from airflow_breeze.utils.path_utils import get_airflow_sources_root
from airflow_breeze.visuals import ASCIIART


def test_visuals():
    assert 2051 == len(ASCIIART)


def test_get_extra_docker_flags():
    airflow_sources = get_airflow_sources_root()
    all = True
    selected = False
    assert len(get_extra_docker_flags(all, selected, str(airflow_sources))) < 10
    all = False
    selected = True
    assert len(get_extra_docker_flags(all, selected, str(airflow_sources))) > 60
    all = False
    selected = False
    assert len(get_extra_docker_flags(all, selected, str(airflow_sources))) < 8
