/*


Client Side (Frontend): React
We have used React to create a clear representation of the end-to-end work of the project. Here, the interface shows an input button to create the tweet, display card to reveal tweets and an option to delete the tweet within display card.

Developer: Jeswanth Vadlamudi

*/

import Head from "next/head";

import {Box,Grid,Heading,Input,Button,Text,Center,Stack,

} from "@chakra-ui/react";

import { useEffect, useState } from "react";

import axios from "axios";





export default function Home() {

  const [text, setText] = useState("");

  const [posts, setPosts] = useState([]);





  useEffect(() => {

    getPosts();

  }, []);





  // Retrieve posts

  const getPosts = async () => {

    const response = await axios.get("https://www.google.com/url?q=http://127.0.0.1:5000/api/posts&source=gmail-imap&ust=1695607170000000&usg=AOvVaw2I4Ake20Z2KqLLJKlkCANh");

    setPosts(response.data);

    console.log(response.data);

  };





  // Create post

  const createPost = async () => {

    await axios.post("https://www.google.com/url?q=http://127.0.0.1:5000/api/posts&source=gmail-imap&ust=1695607170000000&usg=AOvVaw2I4Ake20Z2KqLLJKlkCANh", { text: text });

    setText("");

    getPosts();

  };





  // Delete post

  const deletePost = async (id) => {

    await axios.delete(`http://127.0.0.1:5000/api/posts/${id}`);

    // getPosts();

  };





  return (

    <>

      <Head>

        <title>Twitter clone</title>

        <meta name="description" content="Twitter app" />

        <meta name="viewport" content="width=device-width, initial-scale=1" />

      </Head>

      <Heading m={5} size="lg">

        Black Lotus

      </Heading>

      {posts && (

        <Heading m={5} size="lg">

          Available tweets

        </Heading>

      )}





      <Grid m="5" templateColumns="repeat(3, 1fr)" gap={6}>

        {posts.map((post) => (

          <div key={post.data.id}>

            <Center py={6}>

              <Box

                maxW={"445px"}

                w={"full"}

                bg={"gray.900"}

                boxShadow={"2xl"}

                rounded={"md"}

                p={6}

                overflow={"hidden"}

              >

                <Stack>

                  <Text

                    color={"green.500"}

                    textTransform={"uppercase"}

                    fontWeight={800}

                    fontSize={"sm"}

                    letterSpacing={1.1}

                  >

                    Tweet

                  </Text>

                  <Heading

                    // eslint-disable-next-line react-hooks/rules-of-hooks

                    color={"white"}

                    fontSize={"2xl"}

                    fontFamily={"body"}

                  >

                    {post.data.text}

                  </Heading>

                  <Button

                    colorScheme="red"

                    onClick={() => deletePost(post.data.id)}

                  >

                    Delete Tweet

                  </Button>

                </Stack>

              </Box>

            </Center>

          </div>

        ))} 

      </Grid>

      <Heading ml={5} size="lg">

        Create Tweet

      </Heading>

      <Box maxW="sm" ml="20" overflow="hidden">

        <Input

          mt={5}

          type="text"

          value={text}

          onChange={(e) => setText(e.target.value)}

        />

        <Button type="submit" colorScheme="twitter" mt={5} onClick={createPost}>

          Tweet

        </Button>

      </Box>

    </>

  );

}
