import { Controller, Get, UseGuards } from '@nestjs/common';
import { ProtectedService } from './protected.service';

@Controller('protected')
@UseGuards() // TODO some check for secret keys
export class ProtectedController {
  constructor(private protectedService: ProtectedService) {}

  @Get('unfinished_experiments')
  async getUnfinishedExperiments() {
    return this.protectedService.getAllUnfinishedExperiments();
  }
}
