import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'torloaderControl';
  speed = 0;
  status="initial";

  constructor(public http: HttpClient) {
  }

  public loadJson() {
    this.http.get('/assets/speed.json',
      {headers:{'Cache-Control': 'no-cache'}})
      .subscribe(data => {
        console.log(data)
        this.speed=data["speed"];
      });
  }

  public callRestartTorService(){
    this.http.get('/torloaderControl',
      {headers:{'Cache-Control': 'no-cache'}})
      .subscribe(data => {
        console.log(data)
        this.status=data["status"];
      });
  }
}
