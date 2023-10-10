import { BottomToolbar, Button, Page } from "react-onsenui"
import { YMaps, Map } from "@pbe/react-yandex-maps"
import "onsenui/css/onsenui.css"
import "onsenui/css/onsen-css-components.css"

function App() {
    return (
        <div className="app">
            <Page>
                <YMaps>
                    <div className="department-list-wrapper">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        Minus non quo aspernatur culpa doloribus temporibus
                        quae, architecto quidem provident delectus. Sit quas
                        dicta nesciunt sunt hic nobis repudiandae dolorum.
                        Doloribus.
                    </div>
                    <Map
                        defaultState={{
                            center: [55.75, 37.57],
                            zoom: 9
                        }}
                        className="map-container"
                    />

                </YMaps>
            </Page>
        </div>
    )
}

export default App
