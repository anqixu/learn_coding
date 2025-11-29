#include <iostream>
#include <type_traits>

// Type Lists - manipulate types at compile time
// Implement basic typelist operations

// TODO: Implement TypeList
template<typename... Types>
struct TypeList {};

// TODO: Implement Length metafunction
// template<typename List>
// struct Length;

// TODO: Implement Get metafunction (get type at index)
// template<size_t Index, typename List>
// struct Get;

// TODO: Implement Append metafunction
// template<typename List, typename T>
// struct Append;

int main() {
    using MyList = TypeList<int, double, char>;

    // TODO: Use Length<MyList>::value
    std::cout << "List length: " << 3 << std::endl;

    // TODO: Use Get<0, MyList>::type
    // using FirstType = Get<0, MyList>::type;
    // static_assert(std::is_same_v<FirstType, int>);

    return 0;
}
