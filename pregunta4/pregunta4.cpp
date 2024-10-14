#include <iostream>
#include <cmath>
#include <gtest/gtest.h>

using std::ostream;
using std::cout;
using std::endl;

class Quaternion {
public:
    double a, b, c, d;

    Quaternion(double a, double b, double c, double d) : a(a), b(b), c(c), d(d) {}

    friend ostream& operator<<(ostream& os, const Quaternion& q) {
        os << q.a << " + " << q.b << "i + " << q.c << "j + " << q.d << "k";
        return os;
    }

    // Sobrecarga del operador ==
    bool operator==(const Quaternion& other) const {
        return (a == other.a && b == other.b && c == other.c && d == other.d);
    }

    // Sobrecarga del operador !=
    bool operator!=(const Quaternion& other) const {
        return !(*this == other);
    }


    Quaternion operator+(const Quaternion& other) const {
        
        return Quaternion(a + other.a, b + other.b, c + other.c, d + other.d);
    }

    Quaternion operator+(double scalar) const {
        return Quaternion(a + scalar, b, c, d);
    }
    

    Quaternion operator~() const {
        return Quaternion(a, -b, -c, -d);
    }

    Quaternion operator*(const Quaternion& other) const {
        return Quaternion(
            a * other.a - b * other.b - c * other.c - d * other.d,
            a * other.b + b * other.a + c * other.d - d * other.c,
            a * other.c - b * other.d + c * other.a + d * other.b,
            a * other.d + b * other.c - c * other.b + d * other.a
        );
    }
    
    Quaternion operator*(double scalar) const {
        return Quaternion(a * scalar, b, c, d);
    }
   

    // Sobrecarga del operador & como unario para obtener el valor absoluto
    double operator&() const {
        return std::sqrt(a*a + b*b + c*c + d*d);
    }

};
