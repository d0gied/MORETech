import { BottomToolbar, Button, Page } from 'react-onsenui';
import 'onsenui/css/onsenui.css';
import 'onsenui/css/onsen-css-components.css';

function App() {
  return (
    <div className="app">
      <Page>
        <Button onClick={() => {console.log("Hello!")}}> Tap me!</Button>
        <BottomToolbar >test</BottomToolbar>
      </Page>
    </div>
  )
}

export default App
