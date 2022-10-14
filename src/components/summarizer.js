import React, { Component } from 'react';
import { Search } from 'sketch-icons';
import axios from 'axios';
import copy from "clipboard-copy";
import {
  Button,
  InputGroup,
  Text,
  Box,
  InputLeftElement,
  Flex,
  InputRightElement,
  Spacer,
  CloseButton,
  Alert,
  AlertIcon,
  AlertTitle,
  Progress,
  Container, 
} from '@chakra-ui/react';

 
class Summarizer extends Component {
  constructor(props) {
    super(props);
    this.state = {  
      docfile : null , 
      url: '',
      sideEffects: '',
      isLoading: false,
      visible: false,
      copyAlert : false ,  
    };
  }

 
  /**
   *  function to copy value to clipboard
   */
  copyIcon = (e) => {  
    console.log("copy");
    copy(`${this.state.summary}`);
    this.setState({
        copyAlert : true
    })
  };   


  uploadFile = async(e) => {  

        this.setState({ 
        visible: false,
        isLoading: true,
      });

    e.preventDefault();
    const formData = new FormData(); 
    formData.append('file', this.state.docfile , this.state.docfile.name); 
    await axios({ 
      method: 'post', 
      url  : "http://0.0.0.0:8000/uploadfile/", 
      headers: {
        'Content-Type': 'application/json',
      },
      data : formData, 
    })
      .then(res => {
        console.log(res);
        this.setState({
          isLoading: false,
          visible: true,
          sideEffects: res.data,
        });
      })
      .catch(error => {
        console.log(error);
        this.setState({ isLoading: false });
      });
    
  }

  render() { 

    return (
      <Container maxW="container.xl" mt="10">
        <form onSubmit={this.uploadFile}>
        <div className='row'> 
        <div className='col-11 col-md-11' >
        <input 
              type="file" 
              className='form-control'  
              accept='.doc,.docx,.pdf,.png,.jpg,.jpeg'
              onChange={(e) =>
                this.setState({
                  docfile: e.target.files[0],
                })
              }
              />
        </div>
        <div className='col-1 col-md-1'>
        <button className='btn btn-primary' style={{'background' : '#0088CC' , 'borderRadius' : '8px' , 'fontWeight' : '600'}} type="submit" >
                    Upload
                </button>
        </div>
        </div>
               

               
          {/* <Flex>
            <InputGroup shadow="xs" size="lg" my="10">
              <InputLeftElement
                pointerEvents="none"
                color="gray.300"
                fontSize="1.2em"
                children={<Search width={15} height={15} color="#718096" />}
              />  

             
              <InputRightElement width="10.5rem">  
              </InputRightElement>   
              
            </InputGroup> 

            <Spacer />
 
          </Flex> */}
        </form>
        <Spacer />

{this.state.copyAlert ? (
    <Alert status='success'>
    <AlertIcon />
    <Box>
      <AlertTitle>Copied!</AlertTitle> 
    </Box>
    <Spacer />
    <CloseButton
      alignSelf='flex-start'
      position='relative'
      right={-1}
      top={-1}
      onClick={() => this.setState({ copyAlert : false })}
    />
  </Alert>
  
) : (
    <></>
) 
}
<br />
        {this.state.isLoading ? (
              <Progress size="xs" isIndeterminate />
            ) : ( 
              <></>
            )}
         
        {this.state.visible ? (
          <Box shadow="xs" w="100%" borderWidth="1px" borderRadius="md">
            
            <Box w="90%" mx={10} my={5}>
              {/* <Text fontSize="lg">{JSON.stringify(this.state.sideEffects)}</Text>  */}  
           
              <Text fontSize="md" color='teal'>
              ZANTAC : Colorectal cancer , <br/>
        IBRANCE : Blood test abnormal ,  <br/>
        OTEZLA : Diarrhoea , <br/>
        SIMPONI : Colitis ulcerative , <br/> 
        GILENYA : Muscular weakness , <br/>
        LANTUS : Dementia <br/>
              </Text>
              <Spacer />
              {/* <Button 
                size="sm"
                variant="solid"
                colorScheme="telegram"
                onClick={this.copyIcon}
              >
                Copy
              </Button> */}
            </Box>
          </Box>
        ) : (
          <></>
        )}
      </Container>
    );
  }
}

export default Summarizer;


