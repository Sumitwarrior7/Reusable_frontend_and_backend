import React, { useState } from 'react';
import axios from 'axios';
import { Navigate } from "react-router-dom";

const FormComponent = () => {
  const [name, setName] = useState()
  const [email, setEmail] = useState()
  const [message, setMessage] = useState()

  const handleSubmit = async (event) => {
    event.preventDefault();
    const backendUrl = process.env.REACT_APP_BACKEND_URL;
    const openai_url = backendUrl + "api-app/get-response/"
    const formData = {
      name: name,
      email: email,
      message: message
    }

    try {
      const response = await axios.post(openai_url, formData)
      console.log('API Response:', response.data);

    }
    catch (error) {
      console.error('API Error:', error);
      <Navigate to="/" replace={true} />
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="bg-gray-100 p-6 rounded-lg">
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">Name:</label>
          <input
            type="text"
            name="name"
            onChange={(e) => setName(e.target.value)}
            className="w-full px-3 py-2 rounded-md border focus:outline-none focus:border-blue-500"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">Email:</label>
          <input
            type="email"
            name="email"
            onChange={(e) => setEmail(e.target.value)}
            className="w-full px-3 py-2 rounded-md border focus:outline-none focus:border-blue-500"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">Message:</label>
          <textarea
            name="message"
            onChange={(e) => setMessage(e.target.value)}
            className="w-full px-3 py-2 rounded-md border focus:outline-none focus:border-blue-500"
          />
        </div>
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md focus:outline-none focus:shadow-outline"
        >
          Submit
        </button>
      </form>

    </>
  );
};

export default FormComponent;
