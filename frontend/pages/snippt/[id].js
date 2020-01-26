import fetch from 'isomorphic-fetch';

const Post = props => {
  console.log(`Fetched show: ${props.data.img_url}`);
  return(
    <div className="book-container">
      <p className="title">{props.data.title}</p>
      <div className="img-url">
        <img src={props.data.img_url} />
      </div>
      <p>idioma: {props.data.language }</p>
      <p>estado: {props.data.style }</p>
      <style jsx>{`
        .book-container {
          align-items: center;
          margin: auto;
          text-align: center;
        };
        .img-url {
          margin: auto;
          display: flex;
          justify-content: center;
          height: 400px;
        };
        .img-url img{
          height: 100%
        }
        .title{
          text-decoration: underline;
        }
        p{
          margin-block-start: 0em;
          margin-block-end: 0em;
        }
        `}</style>
    </div>
  )
};

Post.getInitialProps = async function(context) {
  const { id } = context.query;
  const res = await fetch(`http://127.0.0.1:8000/s/snippets/${id}`);
  const data = await res.json();

  return { data };
};

export default Post;