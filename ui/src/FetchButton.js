import React from "react";

const lambdaurl = "https://lsxagerrjkrnvlrub4bx3wcsji0jepov.lambda-url.us-east-2.on.aws/"
const FetchButton = ({ path }) => {
  const handleClick = async () => {
    try {
      const response = await fetch(lambdaurl+path, {
        method: "Get", // or 'GET', 'PUT', 'DELETE', etc.
        headers: {
          "Content-Type": "application/json",
        },
        // body: JSON.stringify({ key: "value" }), // Add body for POST/PUT requests
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Response data:", data);
    } catch (error) {
      console.error("Error making request:", error);
    }
  };

  return <button onClick={handleClick}>Send Request {path}</button>;
};

export default FetchButton;
