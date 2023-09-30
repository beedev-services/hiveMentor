import React from 'react';
import SingleChat from './SingleChat';

const SingleWrapper = (props) => {
  // Pass any props you want to MultiChat here
    return <SingleChat {...props} />;
};

export default SingleWrapper;