"use client";
import React, { useState, ChangeEvent, FormEvent } from "react";
import axios, { AxiosResponse } from "axios";

const ImageUploader: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [responseImage, setResponseImage] = useState<string | null>(null);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files && event.target.files[0];
    setSelectedFile(file || null);
  };

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();

    if (selectedFile) {
      const formData = new FormData();
      formData.append("file", selectedFile);

      try {
        const response: AxiosResponse<Blob> = await axios.post(
          "http://localhost:5000/predictCustom",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
            responseType: "blob",
          }
        );

        if (response.status === 200) {
          const imageURL = URL.createObjectURL(response.data);
          setResponseImage(imageURL);
        } else {
          console.log("Error:", response.status);
        }
      } catch (error) {
        console.log("Error:", error);
      }
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit">Submit</button>
      </form>
      {responseImage && (
        <div>
          <h2>Response Image:</h2>
          <img src={responseImage} alt="Response" />
        </div>
      )}
    </div>
  );
};

export default ImageUploader;
