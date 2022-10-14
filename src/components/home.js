import React from 'react'; 
import { Hero } from './hero';
import Summarizer from './summarizer';
import { 
    Container , Heading , useMediaQuery
} from '@chakra-ui/react'; 
import Footer from './footer';
export const Home = () => {
    const [isMobile] = useMediaQuery("(max-width: 425px)") 

        return ( 
            <> 
            <Hero />
            <Summarizer /> 
            <Footer />
            </>
        ); 
    
} 
