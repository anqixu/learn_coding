#include <iostream>
#include <string>
#include <vector>

// Builder Pattern - HTTP Request Builder
// Implement fluent builder for complex HTTP requests
// Expected output:
//   GET https://api.example.com/users
//   Headers: Authorization: Bearer token123
//   Headers: Accept: application/json
//   POST https://api.example.com/data
//   Headers: Content-Type: application/json
//   Body: {"key":"value"}

class HttpRequest {
    std::string method;
    std::string url;
    std::vector<std::pair<std::string, std::string>> headers;
    std::string body;

public:
    void setMethod(std::string m) { method = m; }
    void setUrl(std::string u) { url = u; }
    void addHeader(std::string key, std::string value) {
        headers.push_back({key, value});
    }
    void setBody(std::string b) { body = b; }

    void print() const {
        std::cout << method << " " << url << std::endl;
        for (const auto& [key, value] : headers) {
            std::cout << "Headers: " << key << ": " << value << std::endl;
        }
        if (!body.empty()) {
            std::cout << "Body: " << body << std::endl;
        }
    }
};

// TODO: Implement HttpRequestBuilder with fluent interface
// Methods should return *this to allow chaining:
// - method(std::string) - sets HTTP method
// - url(std::string) - sets URL
// - header(std::string, std::string) - adds header
// - body(std::string) - sets body
// - build() - returns HttpRequest
class HttpRequestBuilder {
    HttpRequest request;

public:
    HttpRequestBuilder& method(std::string m) {
        // TODO: Set method and return *this
        return *this;
    }

    HttpRequestBuilder& url(std::string u) {
        // TODO: Set URL and return *this
        return *this;
    }

    HttpRequestBuilder& header(std::string key, std::string value) {
        // TODO: Add header and return *this
        return *this;
    }

    HttpRequestBuilder& body(std::string b) {
        // TODO: Set body and return *this
        return *this;
    }

    HttpRequest build() {
        // TODO: Return the built request
        return request;
    }
};

int main() {
    // TODO: Uncomment after implementing builder
    // auto getRequest = HttpRequestBuilder()
    //     .method("GET")
    //     .url("https://api.example.com/users")
    //     .header("Authorization", "Bearer token123")
    //     .header("Accept", "application/json")
    //     .build();
    // getRequest.print();

    // auto postRequest = HttpRequestBuilder()
    //     .method("POST")
    //     .url("https://api.example.com/data")
    //     .header("Content-Type", "application/json")
    //     .body(R"({"key":"value"})")
    //     .build();
    // postRequest.print();

    return 0;
}
