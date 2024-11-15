import { getCurrentInstance } from 'vue';

export default function accessEmitter() {
    return getCurrentInstance().appContext.config.globalProperties.emitter;
}
