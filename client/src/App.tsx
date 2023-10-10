import { Page } from "react-onsenui"
import { YMaps, Map } from "@pbe/react-yandex-maps"
import "onsenui/css/onsenui.css"
import "onsenui/css/onsen-css-components.css"
import SideBar from "./components/sidebar"
import Topbar from "./components/topbar"

export default function App() {
    return (
        <Page className="app">
            <YMaps>
              <div className="ui-wrapper">
                <Topbar />
                <SideBar/>
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
    )
}
