#!/usr/bin/env python3
#
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
#

from unittest import TestCase, main
import pulsar

class DebugLoggerTest(TestCase):

    def test_configure_log_level(self):
        client = pulsar.Client(
            service_url="pulsar://localhost:6650",
            logger=pulsar.ConsoleLogger(pulsar.LoggerLevel.Debug)
        )

        producer = client.create_producer(
            topic='test_log_level'
        )

        producer.send(b'hello')

    def test_configure_log_to_file(self):
        client = pulsar.Client(
            service_url="pulsar://localhost:6650",
            logger=pulsar.FileLogger(pulsar.LoggerLevel.Debug, 'test.log')
        )

        producer = client.create_producer(
            topic='test_log_to_file'
        )

        producer.send(b'hello')

if __name__ == "__main__":
    main()
