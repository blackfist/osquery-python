#  LICENSE file in the root directory of this source tree. An additional grant
#  of patent rights can be found in the PATENTS file in the same directory.

import osquery

@osquery.register_plugin
class MyTablePlugin(osquery.TablePlugin):
    def name(self):
        return "foobar"

    def columns(self):
        return [
            osquery.TableColumn(name="foo", type=osquery.STRING),
            osquery.TableColumn(name="baz", type=osquery.STRING),
        ]

    def generate(self, context):
        query_data = []

        for i in range(2):
            row = {}
            row["foo"] = "bar"
            row["baz"] = "baz"
            query_data.append(row)

        return query_data

if __name__ == "__main__":
    osquery.start_extension()
