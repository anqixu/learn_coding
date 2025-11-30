#include <iostream>
#include <type_traits>

// TypeList - Compile-Time Type Manipulation
// Implement metafunctions to operate on type lists
// Expected output:
//   Length: 3
//   First type is int: true
//   After append: 4
//   Contains double: true

template<typename... Types>
struct TypeList {};

// TODO: Implement Length - get number of types in list
// Specialization for TypeList<Types...>
// Hint: Length<TypeList<int, double>>::value should be 2
template<typename List>
struct Length;

template<typename... Types>
struct Length<TypeList<Types...>> {
    // TODO: static constexpr size_t value = sizeof...(Types);
    static constexpr size_t value = 0;
};

// TODO: Implement Get - get type at index
// Get<0, TypeList<int, double>>::type should be int
// Hint: Use recursion or std::tuple_element trick
template<size_t Index, typename List>
struct Get;

// Base case: Index 0
template<typename Head, typename... Tail>
struct Get<0, TypeList<Head, Tail...>> {
    // TODO: using type = Head;
};

// Recursive case
template<size_t Index, typename Head, typename... Tail>
struct Get<Index, TypeList<Head, Tail...>> {
    // TODO: using type = typename Get<Index-1, TypeList<Tail...>>::type;
};

// TODO: Implement Append - add type to end
// Append<TypeList<int>, double>::type should be TypeList<int, double>
template<typename List, typename T>
struct Append;

template<typename... Types, typename T>
struct Append<TypeList<Types...>, T> {
    // TODO: using type = TypeList<Types..., T>;
};

// TODO: Implement Contains - check if type is in list
// Contains<TypeList<int, double>, double>::value should be true
template<typename List, typename T>
struct Contains;

template<typename T>
struct Contains<TypeList<>, T> {
    // TODO: static constexpr bool value = false;
    static constexpr bool value = false;
};

template<typename Head, typename... Tail, typename T>
struct Contains<TypeList<Head, Tail...>, T> {
    // TODO: static constexpr bool value =
    //   std::is_same_v<Head, T> || Contains<TypeList<Tail...>, T>::value;
    static constexpr bool value = false;
};

int main() {
    using List = TypeList<int, double, char>;

    std::cout << "Length: " << Length<List>::value << std::endl;

    // TODO: Uncomment after implementing Get::type
    // using FirstType = typename Get<0, List>::type;
    // std::cout << "First type is int: "
    //           << (std::is_same_v<FirstType, int> ? "true" : "false") << std::endl;

    // TODO: Uncomment after implementing Append::type
    // using Extended = typename Append<List, float>::type;
    // std::cout << "After append: " << Length<Extended>::value << std::endl;

    std::cout << "Contains double: "
              << (Contains<List, double>::value ? "true" : "false") << std::endl;

    return 0;
}
