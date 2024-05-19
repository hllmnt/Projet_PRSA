/* Generated file, do not edit */

#ifndef CXXTEST_RUNNING
#define CXXTEST_RUNNING
#endif

#define _CXXTEST_HAVE_STD
#include <cxxtest/TestListener.h>
#include <cxxtest/TestTracker.h>
#include <cxxtest/TestRunner.h>
#include <cxxtest/RealDescriptions.h>
#include <cxxtest/TestMain.h>
#include <cxxtest/ErrorPrinter.h>

int main( int argc, char *argv[] ) {
 int status;
    CxxTest::ErrorPrinter tmp;
    CxxTest::RealWorldDescription::_worldName = "cxxtest";
    status = CxxTest::Main< CxxTest::ErrorPrinter >( tmp, argc, argv );
    return status;
}
bool suite_TestMethods_init = false;
#include "/home/valentin-gachon/Documents/PRSA_INPS/PRSA/test/test_solver.h"

static TestMethods suite_TestMethods;

static CxxTest::List Tests_TestMethods = { 0, 0 };
CxxTest::StaticSuiteDescription suiteDescription_TestMethods( "test/test_solver.h", 9, "TestMethods", suite_TestMethods, Tests_TestMethods );

static class TestDescription_suite_TestMethods_testFtcs1 : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_TestMethods_testFtcs1() : CxxTest::RealTestDescription( Tests_TestMethods, suiteDescription_TestMethods, 11, "testFtcs1" ) {}
 void runTest() { suite_TestMethods.testFtcs1(); }
} testDescription_suite_TestMethods_testFtcs1;

static class TestDescription_suite_TestMethods_testFtcs2 : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_TestMethods_testFtcs2() : CxxTest::RealTestDescription( Tests_TestMethods, suiteDescription_TestMethods, 35, "testFtcs2" ) {}
 void runTest() { suite_TestMethods.testFtcs2(); }
} testDescription_suite_TestMethods_testFtcs2;

static class TestDescription_suite_TestMethods_testFtcs3 : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_TestMethods_testFtcs3() : CxxTest::RealTestDescription( Tests_TestMethods, suiteDescription_TestMethods, 62, "testFtcs3" ) {}
 void runTest() { suite_TestMethods.testFtcs3(); }
} testDescription_suite_TestMethods_testFtcs3;

static class TestDescription_suite_TestMethods_testFtcs4 : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_TestMethods_testFtcs4() : CxxTest::RealTestDescription( Tests_TestMethods, suiteDescription_TestMethods, 86, "testFtcs4" ) {}
 void runTest() { suite_TestMethods.testFtcs4(); }
} testDescription_suite_TestMethods_testFtcs4;

#include <cxxtest/Root.cpp>
const char* CxxTest::RealWorldDescription::_worldName = "cxxtest";
