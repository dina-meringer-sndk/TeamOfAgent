<!-- Powered by FVTeamOfAgents Core -->

# Testing Frameworks Knowledge

## Purpose

Comprehensive knowledge base for understanding various testing frameworks and their patterns to enable intelligent test code generation that follows framework-specific best practices and conventions.

## Framework Categories

### **Java Testing Frameworks**

#### **JUnit 5 (Jupiter)**
**Framework Characteristics:**
- Annotation-driven test configuration (@Test, @BeforeEach, @AfterEach)
- Assertions API with rich assertion methods (assertEquals, assertThrows, assertAll)
- Parameterized tests support (@ParameterizedTest, @ValueSource)
- Nested test classes for organized test structure (@Nested)
- Dynamic tests capability for runtime test generation

**Naming Conventions:**
- Test classes: `ClassNameTest` or `TestClassName`
- Test methods: descriptive names with `test` prefix or clear description
- Package structure: mirrors source package with `.test` suffix or separate `test` directory

**Code Generation Patterns:**
```java
@Test
void shouldReturnExpectedValueWhenValidInput() {
    // Arrange
    TargetClass instance = new TargetClass();
    
    // Act
    ResultType result = instance.methodUnderTest(validInput);
    
    // Assert
    assertEquals(expectedValue, result);
}
```

#### **JUnit 4 (Legacy)**
**Framework Characteristics:**
- Annotation-based with @Test, @Before, @After
- Assert class with static methods (Assert.assertEquals)
- @Ignore for skipping tests
- Expected exceptions using @Test(expected = Exception.class)

**Migration Considerations:**
- Different assertion API compared to JUnit 5
- @Before/@After vs @BeforeEach/@AfterEach
- Exception testing syntax differences

### **Python Testing Frameworks**

#### **pytest**
**Framework Characteristics:**
- Simple function-based test definitions (no class inheritance required)
- Assert statements use plain Python assert keyword
- Fixture system for setup/teardown (@pytest.fixture)
- Parameterized tests with @pytest.mark.parametrize
- Plugin ecosystem for extensions

**Naming Conventions:**
- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_function_name`
- Test classes: `TestClassName` (optional, for grouping)

**Code Generation Patterns:**
```python
def test_should_return_expected_value_when_valid_input():
    # Arrange
    instance = TargetClass()
    
    # Act
    result = instance.method_under_test(valid_input)
    
    # Assert
    assert result == expected_value
```

#### **unittest (Standard Library)**
**Framework Characteristics:**
- Class-based test structure inheriting from unittest.TestCase
- setUp/tearDown methods for test preparation
- Rich assertion methods (assertEqual, assertRaises, assertIn)
- Test discovery and runner built-in

**Code Generation Patterns:**
```python
class TestClassName(unittest.TestCase):
    def setUp(self):
        self.instance = TargetClass()
    
    def test_should_return_expected_value(self):
        result = self.instance.method_under_test(valid_input)
        self.assertEqual(expected_value, result)
```

### **JavaScript/TypeScript Testing Frameworks**

#### **Jest**
**Framework Characteristics:**
- describe/it structure for test organization
- Built-in mocking capabilities (jest.fn(), jest.mock())
- Snapshot testing for UI components
- Async testing support (async/await, promises)
- Code coverage reporting built-in

**Code Generation Patterns:**
```javascript
describe('ClassName', () => {
    it('should return expected value when given valid input', () => {
        // Arrange
        const instance = new TargetClass();
        
        // Act
        const result = instance.methodUnderTest(validInput);
        
        // Assert
        expect(result).toBe(expectedValue);
    });
});
```

#### **Mocha + Chai**
**Framework Characteristics:**
- Flexible test structure with describe/it
- Separate assertion library (Chai) with multiple styles
- Async testing with done callback or promises
- Plugin ecosystem for extensions

### **.NET Testing Frameworks**

#### **MSTest**
**Framework Characteristics:**
- Attribute-based testing ([TestMethod], [TestInitialize], [TestCleanup])
- Assert class with static methods
- Test categories and grouping support
- Visual Studio integration

#### **NUnit**
**Framework Characteristics:**
- Rich attribute system ([Test], [SetUp], [TearDown])
- Fluent assertion syntax (Assert.That)
- Parameterized tests support ([TestCase])
- Constraint-based assertions

**Code Generation Patterns:**
```csharp
[Test]
public void ShouldReturnExpectedValueWhenValidInput()
{
    // Arrange
    var instance = new TargetClass();
    
    // Act
    var result = instance.MethodUnderTest(validInput);
    
    // Assert
    Assert.That(result, Is.EqualTo(expectedValue));
}
```

## Framework Detection Strategies

### **File-Based Detection**
- **Java**: Look for `pom.xml`, `build.gradle`, or `build.xml` with testing dependencies
- **Python**: Check `requirements.txt`, `setup.py`, or `pyproject.toml` for test frameworks
- **JavaScript**: Examine `package.json` for testing library dependencies
- **.NET**: Review project files (`.csproj`, `.fsproj`) for test package references

### **Directory Structure Analysis**
- **Maven/Gradle**: `src/test/java` directory structure
- **Python**: `tests/` directory or `test_*.py` files
- **Node.js**: `test/` or `__tests__/` directories
- **.NET**: Separate test projects or `Tests` folders

### **Import/Using Statement Analysis**
- Scan existing test files for framework-specific imports
- Identify assertion library usage patterns
- Detect mocking framework preferences
- Understand test runner configurations

## Best Practices by Framework

### **Universal Best Practices**
- **Arrange-Act-Assert Pattern**: Clear separation of test phases
- **Descriptive Test Names**: Test intent clearly expressed in method names
- **Single Responsibility**: Each test validates one specific behavior
- **Test Independence**: Tests should not depend on execution order
- **Meaningful Assertions**: Validate actual business requirements

### **Framework-Specific Patterns**
- **JUnit**: Use @DisplayName for complex test descriptions
- **pytest**: Leverage fixtures for shared setup, parametrize for data-driven tests
- **Jest**: Use describe blocks for logical grouping, beforeEach for setup
- **MSTest/NUnit**: Utilize test categories for test organization

## Integration Considerations

### **Build System Integration**
- **Maven**: Surefire plugin configuration for test execution
- **Gradle**: Test task configuration and reporting
- **npm**: Test scripts and coverage reporting setup
- **MSBuild**: Test adapter configuration and discovery

### **CI/CD Integration**
- Test execution commands for different frameworks
- Test result reporting formats (JUnit XML, TAP, etc.)
- Coverage reporting integration
- Parallel execution capabilities

### **IDE Integration**
- Test discovery and execution support
- Debugging capabilities for different frameworks
- Code coverage visualization
- Test result display and navigation

## Framework Evolution and Migration

### **Version Compatibility**
- Breaking changes between framework versions
- Migration guides and compatibility considerations
- Deprecated features and recommended alternatives
- New feature adoption strategies

### **Multi-Framework Support**
- Projects using multiple testing frameworks
- Framework selection criteria for different test types
- Integration strategies for mixed environments
- Migration planning and execution