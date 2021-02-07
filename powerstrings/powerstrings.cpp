#include <iostream>
#include <string>
using namespace std;

int main() {
   string input;
   std::string_view input_view;
   int stepSize;
   int length;
   int sqrtLength;
   bool valid;
   bool found;

   while (cin >> input) {
      if (input == ".") {
         return 0;
      }
      input_view = input;
      length = input_view.size();
      found = false;
      for (int i = 1; i*i <= length; i++) {
         sqrtLength = i;
         if (length % i == 0) {
            int n = length / i;
            stepSize = length / n;
            valid = true;
            for (int j = 1; j < n; j++) {
               if (input_view.substr(0, stepSize) != input_view.substr(j*stepSize, stepSize)) {
                  valid = false;
                  break;
               }
            }
            if (valid) {
               found = true;
               cout << n << "\n";
               break;
            }
         }
      }
      if (found) {
         continue;
      }
      for (int n = sqrtLength; n > 1; n--) {
         if (n*n == length) {
            continue;
         }
         if (length % n == 0) {
            stepSize = length / n;
            valid = true;
            for (int j = 1; j < n; j++) {
               if (input_view.substr(0, stepSize) != input_view.substr(j*stepSize, stepSize)) {
                  valid = false;
                  break;
               }
            }
            if (valid) {
               found = true;
               cout << n << "\n";
               break;
            }
         }
      }
      if (found) {
         continue;
      }
      cout << "1\n";
   }
}