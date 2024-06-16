import React, { useState, useEffect } from "react";
import { Form, Button } from "react-bootstrap";

const EmailForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [body, setBody] = useState("");
  const [title, setTitle] = useState("");
  const [attachmentPath, setAttachmentPath] = useState("");

  useEffect(() => {
    fetchDefaultData();
  }, []);

  const fetchDefaultData = async () => {
    try {
      const response = await fetch("/default_data");
      const data = await response.json();
      setBody(data.body);
      setAttachmentPath(data.attachmentPath);
    } catch (error) {
      console.error("Error fetching default data:", error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("/send_email", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password, body, title, attachmentPath }),
      });

      const data = await response.text();
      console.log(data);
      // Reset form fields or show a success message
    } catch (error) {
      console.error("Error sending email:", error);
      // Show an error message
    }
  };

  return (
    <div className='min-h-screen bg-gray-100 flex justify-center items-center'>
      <div className='bg-white p-8 rounded-lg shadow-md max-w-md w-full'>
        <h2 className='text-2xl font-bold mb-6 text-center'>Email Sender</h2>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId='formEmail' className='mb-4'>
            <Form.Label className='font-semibold mb-1'>Email</Form.Label>
            <Form.Control
              type='email'
              placeholder='Enter email'
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className='rounded-md'
            />
          </Form.Group>

          <Form.Group controlId='formPassword' className='mb-4'>
            <Form.Label className='font-semibold mb-1'>Password</Form.Label>
            <Form.Control
              type='password'
              placeholder='Enter password'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className='rounded-md'
            />
          </Form.Group>

          <Form.Group controlId='formBody' className='mb-4'>
            <Form.Label className='font-semibold mb-1'>Body</Form.Label>
            <Form.Control
              as='textarea'
              rows={3}
              placeholder='Enter email body'
              value={body}
              onChange={(e) => setBody(e.target.value)}
              className='rounded-md'
            />
          </Form.Group>
          <Form.Group controlId='formTitle' className='mb-6'>
            <Form.Label className='font-semibold mb-1'>Title</Form.Label>
            <Form.Control
              type='text'
              placeholder='Enter email title'
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className='rounded-md'
            />
          </Form.Group>
          <Button
            variant='primary'
            type='submit'
            className='w-full rounded-md py-2 font-semibold'
          >
            Send Email
          </Button>
        </Form>
      </div>
    </div>
  );
};

export default EmailForm;
