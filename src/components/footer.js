import {Text , Box  ,Code , Stack , Image ,   useColorModeValue  , Spacer , Button , Flex, Container} from "@chakra-ui/react";
 
const Footer = () => {

    const style = {
        fontFamily: "system-ui",
        position: 'fixed',
        bottom: '0',
        left: '0',
        zIndex: '9',
        width: '100%',
    }

  const textColor = useColorModeValue('gray.600' , 'gray.600')

    return (
        <Box style={style} bg="gray.100" px="10" py="5">
            <Container maxW='container.xl'>
            <Flex alignItems="center" >
           <Stack direction="row" isInline>
          <Image
            boxSize="35px"
            objectFit="contain"
            src="https://firebasestorage.googleapis.com/v0/b/react-firechat-ae4bf.appspot.com/o/icons8-medical-64.png?alt=media&token=ee062f7a-f541-4e01-885e-ab266ea9e766"             
            alt="Turtle Text"
          />
          <Text size="lg" color={textColor} >Swapn &nbsp;
          <Spacer />
          <span>
            <Code colorScheme={textColor} color="gray">v0.1.1</Code>
          </span> 
          </Text>
          
        </Stack> 
        <Spacer />
        <Text fontSize='sm' color={textColor} >
       Proudly built with ❤️ in India 
        </Text>
        <Spacer />
        <Text fontSize='sm' color={textColor}>
       Released under MIT License | Copyright @ 2022
        </Text>
        </Flex>
        </Container>
        </Box>
    );
}
export default Footer;
 