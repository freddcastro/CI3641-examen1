#include <gtest/gtest.h>
#include "pregunta4.cpp"

TEST(QuaternionTest, Addition) {
    Quaternion q1(1, 2, 3, 4);
    Quaternion q2(1, 2, 3, 4);
    Quaternion expected(2, 4, 6, 8);
    EXPECT_EQ(q1 + q2, expected);
}

TEST(QuaternionTest, ScalarAddition) {
    Quaternion q(1, 2, 3, 4);
    Quaternion expected(4, 2, 3, 4);
    EXPECT_EQ(q + 3, expected);
}

TEST(QuaternionTest, Conjugate) {
    Quaternion q(1, 2, 3, 4);
    Quaternion expected(1, -2, -3, -4);
    EXPECT_EQ(~q, expected);
}

TEST(QuaternionTest, Multiplication) {
    Quaternion q1(1, 2, 3, 4);
    Quaternion q2(1, 2, 3, 4);
    Quaternion expected(-28, 4, 6, 8);
    EXPECT_EQ(q1 * q2, expected);
}

TEST(QuaternionTest, ScalarMultiplication) {
    Quaternion q(1, 2, 3, 4);
    Quaternion expected(3.1, 2, 3, 4);
    EXPECT_EQ(q * 3.1, expected);
}

TEST(QuaternionTest, AbsoluteValue) {
    Quaternion q(1, 2, 3, 4);
    double expected = std::sqrt(30);
    EXPECT_DOUBLE_EQ(&q, expected);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}