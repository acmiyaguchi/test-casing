#include <iostream>
#include <string>
#include <vector>

using namespace std;

static string hive_name(const string &name)
{
  vector<char> v;
  size_t len = name.size();
  bool upper = true;
  for (size_t i = 0; i < len; ++i) {
    if (isupper(name[i])) {
      if (!upper) {
        v.push_back('_');
      }
      upper = true;
      v.push_back(tolower(name[i]));
    } else {
      if (isalnum(name[i])) {
        upper = false;
        v.push_back(name[i]);
      } else {
        upper = true;
        v.push_back('_');
      }
    }
  }
  return string(v.begin(), v.end());
}

int main() {
    for (string line; getline(cin, line);) {
        cout << hive_name(line) << endl;
    }
    return 0;
}