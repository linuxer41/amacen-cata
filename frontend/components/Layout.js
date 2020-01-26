import Header from './Header';
const layoutStyle = {
  margin: 20,
  padding: 20,
  border: '1px solid #DDD'
};
const Layout = props => {
  return(
    <div style={layoutStyle}>
      <Header />
      {props.children}
      <style jsx>{`
        .layout {
          margin: 20;
          padding: 20;
          border: '1px solid #DDD';
        }
        p {
          color: blue;
        }
      `}</style>
      <style jsx global>{`
        body {
          margin: 0;
          padding: 0;
          font-size: 18px;
          font-weight: 400;
          line-height: 1.8;
          color: #333;
          font-family: sans-serif;
        }
        h1 {
          font-weight: 700;
        }
        p {
          margin-bottom: 10px;
        }
        a {
          text-decoration: none;
          color: black
        }
      `}</style>
    </div>
    
  )
};

export default Layout;