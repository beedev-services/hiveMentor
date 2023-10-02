import React from 'react';
import MultiChat from './MultiChat';

const MultiWrapper = (theUser) => {
  // Pass any props you want to MultiChat here

  console.log('what is props on multiwrapper:', theUser)
    return <MultiChat theUser = {theUser} />;
};

export default MultiWrapper;